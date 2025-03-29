from flask import render_template, url_for, flash, redirect, request, jsonify, abort
from flask_login import login_user, current_user, logout_user, login_required
from app import db
from models import User, SavedExam
from forms import RegistrationForm, LoginForm, SearchForm, ChatbotForm
from chatbot import chatbot
from data import (
    get_exam_categories, 
    get_exams_by_category, 
    get_exam_details, 
    search_exams,
    EXAM_CATEGORIES,
    EXAMS_DATA
)

def register_routes(app):
    
    @app.context_processor
    def inject_search_form():
        return {'search_form': SearchForm()}
    
    @app.route('/')
    @app.route('/home')
    def home():
        categories = get_exam_categories()
        return render_template('index.html', title='Home', categories=categories)
    
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if current_user.is_authenticated:
            return redirect(url_for('home'))
        
        form = RegistrationForm()
        if form.validate_on_submit():
            user = User(username=form.username.data, email=form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Your account has been created! You can now log in.', 'success')
            return redirect(url_for('login'))
        
        return render_template('register.html', title='Register', form=form)
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('home'))
        
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            
            if user and user.check_password(form.password.data):
                login_user(user, remember=form.remember.data)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('home'))
            else:
                flash('Login unsuccessful. Please check email and password.', 'danger')
        
        return render_template('login.html', title='Login', form=form)
    
    @app.route('/logout')
    def logout():
        logout_user()
        flash('You have been logged out.', 'info')
        return redirect(url_for('home'))
    
    @app.route('/profile')
    @login_required
    def profile():
        saved_exams = SavedExam.query.filter_by(user_id=current_user.id).all()
        exams_details = []
        
        for saved in saved_exams:
            exam = get_exam_details(saved.exam_id)
            if exam:
                exams_details.append(exam)
        
        return render_template('profile.html', title='Profile', 
                               user=current_user, saved_exams=exams_details)
    
    @app.route('/category/<string:category_id>')
    def exam_category(category_id):
        category_data = next((c for c in get_exam_categories() if c['id'] == category_id), None)
        
        if not category_data:
            abort(404)
            
        exams = get_exams_by_category(category_id)
        return render_template('exam_category.html', title=category_data['name'],
                              category=category_data, exams=exams)
    
    @app.route('/exam/<string:exam_id>')
    def exam_detail(exam_id):
        exam = get_exam_details(exam_id)
        
        if not exam:
            abort(404)
            
        is_saved = False
        if current_user.is_authenticated:
            saved = SavedExam.query.filter_by(
                user_id=current_user.id, 
                exam_id=exam_id
            ).first()
            is_saved = saved is not None
            
        return render_template('exam_detail.html', title=exam['name'],
                              exam=exam, is_saved=is_saved)
    
    @app.route('/save_exam/<string:exam_id>', methods=['POST'])
    @login_required
    def save_exam(exam_id):
        # Check if the exam exists
        exam = get_exam_details(exam_id)
        if not exam:
            return jsonify({'success': False, 'message': 'Exam not found'}), 404
            
        # Check if already saved
        existing = SavedExam.query.filter_by(
            user_id=current_user.id, 
            exam_id=exam_id
        ).first()
        
        if existing:
            return jsonify({'success': False, 'message': 'Exam already saved'}), 400
            
        # Save the exam
        saved_exam = SavedExam(user_id=current_user.id, exam_id=exam_id)
        db.session.add(saved_exam)
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Exam saved successfully'})
    
    @app.route('/unsave_exam/<string:exam_id>', methods=['POST'])
    @login_required
    def unsave_exam(exam_id):
        saved_exam = SavedExam.query.filter_by(
            user_id=current_user.id, 
            exam_id=exam_id
        ).first()
        
        if not saved_exam:
            return jsonify({'success': False, 'message': 'Exam not saved'}), 404
            
        db.session.delete(saved_exam)
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Exam removed from saved list'})
    
    @app.route('/search', methods=['GET', 'POST'])
    def search():
        form = SearchForm()
        results = []
        
        if form.validate_on_submit() or request.args.get('query'):
            query = form.query.data if form.validate_on_submit() else request.args.get('query')
            results = search_exams(query)
            
        return render_template('search_results.html', title='Search Results',
                              query=request.args.get('query', ''), results=results)
    
    @app.route('/chatbot-page')
    def chatbot_page():
        """Render the chatbot HTML page with exam data loaded for client-side processing"""
        categories = EXAM_CATEGORIES
        exams_data = EXAMS_DATA
        return render_template('chatbot.html', title='ExamSeek Chatbot', 
                              categories=categories, exams_data=exams_data)

    @app.route('/chatbot', methods=['POST'])
    def chatbot_query():
        message = request.json.get('message', '')
        
        if not message:
            return jsonify({'error': 'No message provided'}), 400
            
        response = chatbot.get_response(message)
        return jsonify(response)
    
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html', title='Page Not Found'), 404
    
    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('500.html', title='Server Error'), 500
