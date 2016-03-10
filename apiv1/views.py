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

from django.utils import timezone
from django.core.cache import cache
from django.conf import settings
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
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    paginate_by = 10

    def get_queryset(self):
        now = timezone.now()
        return News.objects.filter(date__lte=now).order_by('date').reverse()


class MagCreateReadView(NewsCreateReadView):

    def get_queryset(self):
        now = timezone.now()
        return News.objects.filter(date__lte=now).filter(mag=1).order_by('date').reverse()


class NewsReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        now = timezone.now()
        return News.objects.filter(date__lte=now).order_by('date').reverse()


class NewsAdminCreateReadView(ListCreateAPIView):
    queryset = News.objects.all().order_by('date').reverse()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    paginate_by = 10

    def pre_save(self, obj):
        obj.author = self.request.user.name


class NewsAdminReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def pre_save(self, obj):
        obj.author = self.request.user.name


class AdsCreateReadView(ListCreateAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        ads = []
        placeholder = self.request.GET.get('placeholder', '')
        ads_placeholders = getattr(settings, 'ADS_PLACEHOLDERS', None)

        if placeholder == '' or placeholder in dict(ads_placeholders).keys():
            category = self.request.GET.get('category', None)

            if category is not None:
                ads = Ads.objects.by_placeholder_and_category(
                    placeholder,
                    category
                )
            else:
                ads = Ads.objects.all()

        return ads


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
        now = timezone.now()
        return BlogPosts.objects.filter(blogId=blogger).filter(date__lte=now).order_by('date').reverse()


class BlogPostsReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = BlogPostsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        blogger = self.kwargs['blogger']
        id = self.kwargs['pk']
        now = timezone.now()
        return BlogPosts.objects.filter(blogId=blogger).filter(id=id).filter(date__lte=now)


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
    queryset = Races.objects.all().order_by('date').reverse()
    paginate_by = 20


class RacesCategoryCreateReadView(RacesCreateReadView):

    def get_queryset(self):
        category = self.kwargs['category']
        page = self.request.GET.get('page')
        if page is not None and int(page) in [1, 2, 3, 4]:
            page = int(page)
            key = 'race' + category
            start = 0
            end = (5 * self.paginate_by)
            if cache.get(key) is None:
                races = Races.objects.filter(
                    category=category).order_by('date').reverse()
                cache.set(key, races, 3600)
            return cache.get(key)[start:end]
        return Races.objects.filter(category=category).order_by('date').reverse()


class RacesReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = RacesSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Races.objects.all().order_by('date')


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
