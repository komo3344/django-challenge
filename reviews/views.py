from django.shortcuts import render, redirect, reverse
from .models import Review
from .forms import ReviewForm
from movies.models import Movie
from books.models import Book


def review_add(request, pk):
    kind = request.GET.get('kind', 'movie')
    if request.method == 'POST':
        ReviewForm(request.POST)
        text = request.POST.get('text')
        rating = request.POST.get('rating')
        if kind == 'movie':
            movie = Movie.objects.get(pk=pk)
            Review.objects.get_or_create(created_by=request.user, text=text, rating=rating, movie=movie)
            return redirect(reverse('movies:movie', kwargs={'pk': pk}))
        else:
            book = Book.objects.get(pk=pk)
            Review.objects.get_or_create(created_by=request.user, text=text, rating=rating, book=book)
            return redirect(reverse('movies:movie', kwargs={'pk': pk}))
    else:
        form = ReviewForm()
        return render(request, 'reviews/form.html', {
            'form': form
        })


def review_remove(request, pk):
    kind = request.GET.get('kind', 'movie')
    review = Review.objects.get(pk=pk)
    review.delete()
    if kind == 'movie':
        movie = review.movie
        return redirect(reverse('movies:movie', kwargs={'pk': movie.pk}))
    else:
        book = review.book
        return redirect(reverse('core:home', kwargs={'pk': book.pk}))
