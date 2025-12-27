from django.db.models import QuerySet

from db.models import MovieSession, CinemaHall, Movie
from datetime import datetime


def create_movie_session(movie_show_time: str,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:

    return MovieSession.objects.create(show_time=movie_show_time,
                                       cinema_hall=CinemaHall.objects
                                       .get(id=cinema_hall_id),
                                       movie=Movie.objects.get(id=movie_id))


def get_movies_sessions(session_date: str = None) -> QuerySet[MovieSession]:
    if session_date:
        date_obj = datetime.strptime(session_date, "%Y-%m-%d").date()
        return MovieSession.objects.filter(show_time__date=date_obj)
    else:
        return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: str = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> None:
    if show_time:
        (MovieSession.objects.filter(id=session_id)
         .update(show_time=show_time))
    if movie_id:
        (MovieSession.objects.filter(id=session_id)
         .update(movie=Movie.objects.get(id=movie_id)))
    if cinema_hall_id:
        (MovieSession.objects.filter(id=session_id)
         .update(cinema_hall=CinemaHall.objects.get(id=cinema_hall_id)))


def delete_movie_session_by_id(session_id: int) -> None:
    if session_id:
        MovieSession.objects.get(id=session_id).delete()
