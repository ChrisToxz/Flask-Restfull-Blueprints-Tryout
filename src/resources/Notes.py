from flask_restful import Resource

from src.handlers.notehandler import NoteHandler

class Notes(Resource):

    def post(self):
        #Call handler to create note
        return NoteHandler.create()