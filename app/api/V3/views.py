import datetime
import time

from flask_restful import Resource
from flask import request, make_response, jsonify

rental_list = []


class Bookings(Resource):
    """docstring for Bookings"""

    def post(self):
        """creating a booking"""
        req = request.get_json()
        new = {
            "id": len(rental_list) + 1,
            "title": req['title'],
            "description": req['description'],
            "days": req['days'],
            "books" : req['books']
        }
        if (new['description'] == "Fiction"):
            Total = (new['books'] * new['days'])  + (new['days'] * 3 * new['books'])
        elif (new['description'] == "Regular"):
            if (new['days'] < 2):
                Total = (new['books'] * 2 )
            else:
                Total = (new['books'] * 2 * 1) + ((new['days'] - 2) * 1.5 * new['books'])
            #Total = (new['books'] * new['days'])  + (new['days'] * 1.5 * new['books'])
        elif (new['description'] == "Novel"):
            if (new['days'] < 3):
                Total = (new['books'] * 4.5 )
            else:
                Total = (new['books'] * new['days'])  + (new['days'] * 1.5 * new['books'])
        else:
            Total = new['books'] * new['days']
        rental_list.append(new)
        return make_response(jsonify({
            "msg": "Rented",
            "rental_id": new['id'],
            "Total" : Total
        }), 201)

    def get(self):
        """retrieving all blogs"""
        return make_response(jsonify({
            "msg": "ok",
            "bookings": rental_list
        }), 200)


class SingleBooking(Resource):
    """docstring for SingleBooking"""

    def get(self, id):
        """retrieving a single booking based on id"""
        for rental in rental_list:
            if rental['id'] == id:
                my_rental = rental
                return make_response(jsonify({
                    "msg": "ok",
                    "rental": my_rental
                }), 200)

            return make_response(jsonify({
                "msg": "Not found"
            }), 404)

    def delete(self, id):
        """deleting a single booking based on id"""
        for rental in rental_list:
            if rental['id'] == id:
                rental_list.remove(rental)
                return make_response(jsonify({
                "msg": "Booking with id {} id deleted".format(id),
                "rental" : rental
                }), 200)
            else:
                return make_response(jsonify({
                "msg": "Booking with id {} id not found".format(id) 
                }), 404)

    def put(self, id):
        """editing a single blog based on id"""
        for rental in rental_list:
            if rental['id'] == id:
                req = request.get_json()
                rental['title'] = req['title']
                rental['description'] = req['description']
                #rental['updated'] = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
                return make_response(jsonify({
                    "msg": "ok",
                    "booking": rental
                }), 200)

            updated_booking = {
                "id": id,
                "tittle": req['tittle'],
                "description": req['description'],
                "days": req['days'],
                "books" : req['books']
                #"updated": datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            }
            rental_list.append(updated_booking)

            return make_response(jsonify({
                "msg": "ok",
                "booking": rental
}), 201)