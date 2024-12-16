from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy-Auftragsdaten (als Speicher für Aufträge)
orders = []

@app.route('/')
def index():
    """Startseite: Zeigt alle Aufträge an."""
    return render_template('index.html', orders=orders)

@app.route('/add', methods=['GET', 'POST'])
def add_order():
    """Seite zum Hinzufügen neuer Aufträge."""
    if request.method == 'POST':
        # Neue Auftragsdaten aus dem Formular
        name = request.form.get('name')
        description = request.form.get('description')
        if name and description:
            # Auftrag hinzufügen
            orders.append({'name': name, 'description': description})
            return redirect(url_for('index'))
    return render_template('add_order.html')

if __name__ == '__main__':
    app.run(debug=True)
