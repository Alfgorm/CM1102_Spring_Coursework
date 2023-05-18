from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm
import sqlite3
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from wtforms import ValidationError
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'


#For validtion of the checkout field
class PaymentForm(FlaskForm):
    card_number = StringField("Enter your 16 digit card number", validators=[DataRequired(), Length(min = 16, max =16)])
    name = StringField("Enter the name on the card", validators=[DataRequired()]) 
    cvv = StringField("Enter your CVV", validators=[DataRequired(), Length(min = 3, max = 3)])
    expiration_date = StringField("Enter the expiration date as MM/YY", validators=[DataRequired(),])

    submit = SubmitField('Submit')
    
    def validate_expiration_date(self, field):
        # Check to make sure the expiration date is in the format MM/YY
        if not re.match(r'^\d{2}/\d{2}$', field.data):
            raise ValidationError('Invalid expiration date format. Please use MM/YY format.')
    

@app.route('/')
def index():
    sort_by = request.args.get('sort-by')
    conn = sqlite3.connect('For SQLite/mydb.db')
    cursor = conn.cursor()
    if sort_by == 'price':
        cursor.execute('SELECT * FROM products WHERE prod_id != 10 ORDER BY prod_price ASC')
    elif sort_by == 'name':
        cursor.execute('SELECT * FROM products WHERE prod_id != 10 ORDER BY prod_name ASC')
    
    else:
        cursor.execute('SELECT * FROM products WHERE prod_id != 10')
    
    
    data = cursor.fetchall()
    conn.close()
    
    return render_template('index.html', data=data)
    

@app.route('/page2')
def page2():
    conn = sqlite3.connect('For SQLite/mydb.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM products WHERE prod_id = 10')
    product = cursor.fetchone()

    conn.close()
    
    return render_template('page2.html', product=product)

@app.route('/page3')
def page3():
    conn = sqlite3.connect('For SQLite/mydb.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cart")
    cart_items = cursor.fetchall()
    cursor.execute("SELECT SUM(prod_price) FROM cart")
    total_price = cursor.fetchone()[0]
    conn.close()
    return render_template('page3.html', cart_items=cart_items, total_price=total_price)
    
    
    

@app.route('/page4', methods=['GET', 'POST'])
def page4():
    form = PaymentForm()
    if form.validate_on_submit():
        card_number = form.card_number.data
        name = form.name.data
        cvv = form.cvv.data
        expiration_date = form.expiration_date.data
        return render_template('page5.html', card_number = card_number, name = name, cvv = cvv, expiration_date = expiration_date) 
    return render_template('page4.html', form = form)

@app.route('/page5')
def page5():
    return render_template('page5.html')

@app.errorhandler(404)                      
def not_found(e):
    return render_template('404.html'), 404

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product_id = request.form.get('product_id')

    
    conn = sqlite3.connect('For SQLite/mydb.db')
    cursor = conn.cursor()
    
    try:
        #This is retreiving information from the products table
        cursor.execute("SELECT prod_name, prod_price FROM products WHERE prod_id=?", (product_id,))
        product = cursor.fetchone()

        if product:
            product_name = product[0]
            product_price = product[1]

            cursor.execute("INSERT INTO cart (prod_id, prod_name, prod_price) VALUES (?, ?, ?)",
                        (product_id, product_name, product_price))

            cursor.execute("SELECT SUM(prod_price) FROM cart")
            total_price = cursor.fetchone()[0]
            conn.commit()
            conn.close()
            flash("Product added to cart", "success")
            
        else:
            flash("Product not found", "error")
            
    except Exception as e:
        conn.rollback()
        flash("An error occurred while adding the product to cart", "error")

    finally:
        conn.close()

    return redirect(request.referrer or '/')
        
@app.route('/remove_from_cart/<int:product_id>', methods=['POST'])
def remove_from_cart(product_id):
    
    conn = sqlite3.connect('For SQLite/mydb.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cart WHERE prod_id=?", (product_id,))
    conn.commit()
    conn.close()

    return redirect('/page3')

    


if __name__ == "__main__":
    app.run(debug=True)
    

