from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
)

from apiv1.serializers import (
    NewsSerializer,
    AdsSerializer,
    BloggersSerializer,
    BlogPostsSerializer,
    SkiclubsSerializer,
    PagesSerializer,
    RacesSerializer,
    WidgetsSerializer,
    CoversSerializer,
)

from datetime import datetime

from news.models import News
from ads.models import Ads
from skiclubs.models import Skiclubs
from pages.models import Pages
from rankings.models import Races
from widgets.models import Widgets
from angulation.models import Covers
from blogs.models import (
    Bloggers,
    BlogPosts,
)


class NewsCreateReadView(ListCreateAPIView):
    queryset = News.objects.filter(
        date__lte=datetime.now).order_by('date').reverse()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    paginate_by = 10


class MagCreateReadView(NewsCreateReadView):
    queryset = News.objects.filter(date__lte=datetime.now).filter(
        mag=1).order_by('date').reverse()


class NewsReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = News.objects.filter(date__lte=datetime.now)
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class NewsAdminCreateReadView(ListCreateAPIView):
    queryset = News.objects.all().order_by('date').reverse()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    paginate_by = 10


class NewsAdminReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class AdsCreateReadView(ListCreateAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        if self.request.GET.get('category'):
            cat = self.request.GET.get('category')
            if cat == 'square':
                return Ads.objects.filter(square=1)
            if cat == 'horizontal':
                return Ads.objects.filter(horizontal=1)
            if cat == 'vertical':
                return Ads.objects.filter(vertical=1)
        return Ads.objects.all()


class AdsReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class BloggersCreateReadView(ListCreateAPIView):
    queryset = Bloggers.objects.all().order_by('date').reverse()
    serializer_class = BloggersSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class BloggersReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Bloggers.objects.all()
    serializer_class = BloggersSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class BlogPostsCreateReadView(ListCreateAPIView):
    serializer_class = BlogPostsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        blogger = self.kwargs['blogger']
        return BlogPosts.objects.filter(blogId=blogger).filter(date__lte=datetime.now).order_by('date').reverse()


class BlogPostsReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = BlogPostsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        blogger = self.kwargs['blogger']
        id = self.kwargs['pk']
        return BlogPosts.objects.filter(blogId=blogger).filter(id=id).filter(date__lte=datetime.now)


class SkiclubsCreateReadView(ListCreateAPIView):
    serializer_class = SkiclubsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Skiclubs.objects.all().order_by('title')


class SkiclubsReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = SkiclubsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Skiclubs.objects.all().order_by('title')


class PagesCreateReadView(ListCreateAPIView):
    serializer_class = PagesSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Pages.objects.all().order_by('id')


class PagesReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = PagesSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Pages.objects.all().order_by('id')


class RacesCreateReadView(ListCreateAPIView):
    serializer_class = RacesSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Races.objects.all().order_by('raceId')


class RacesCategoryCreateReadView(ListCreateAPIView):
    serializer_class = RacesSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        category = self.kwargs['category']
        return Races.objects.filter(category=category).order_by('raceId')


class RacesReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = RacesSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Races.objects.all().order_by('raceId')


class WidgetsCreateReadView(ListCreateAPIView):
    queryset = Widgets.objects.all()
    serializer_class = WidgetsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class WidgetsReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Widgets.objects.all()
    serializer_class = WidgetsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class CoversCreateReadView(ListCreateAPIView):
    queryset = Covers.objects.all()
    serializer_class = CoversSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class CoversReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Covers.objects.all()
    serializer_class = CoversSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
