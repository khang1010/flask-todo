from app import app, db
from app.models import Todo
from flask import jsonify, request

@app.route('/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.order_by(Todo.date_created).all()
    result = [{'task': todo.task, 'completed': todo.completed, 'id': todo.id, 'date_created': todo.date_created} for todo in todos]
    return jsonify(result)

@app.route('/todos', methods=['POST'])
def create_todo():
    try:
        task = request.json.get('task')
        completed = request.json.get('completed', False)
        
        new_todo = Todo(task=task, completed=completed)
        db.session.add(new_todo)
        db.session.commit()
        return jsonify({'message': 'Todo created successfully!'}), 201
    except Exception as e:
        error = str(e)
        return jsonify(error), 400
    
@app.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    try:
        todo = Todo.query.get(id)
    
        if not todo:
            return jsonify({'message': 'Todo not found!'}), 404
        
        task = request.json.get('task')
        completed = request.json.get('completed')
        
        todo.task = task if task is not None else todo.task
        todo.completed = completed if completed is not None else todo.completed   
        
        db.session.commit()
        
        return jsonify({'message': "Update successfully!", 'metadata': {'task': todo.task, 'completed': todo.completed}}), 200
    except Exception as e:
        error = str(e)
        return jsonify(error), 400
    
@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    try:
        todo = Todo.query.get(id)
    
        if not todo:
            return jsonify({'message': 'Todo not found!'}), 404
        
        db.session.delete(todo)
        db.session.commit()
        
        return jsonify({'message': 'Deleted successfully!'}), 200
    except Exception as e:
        error = str(e)
        return jsonify(error), 400