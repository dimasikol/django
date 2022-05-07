from django.urls import path
from .views import category,subcategory,item,show_quiz,lk_view
urlpatterns = [
    path('category/<int:pk>/<int:id>/<slug:url>/', item.ItemView.as_view(), name='item_view'),
    path('category/<int:pk>/<int:id>/', item.ItemListView.as_view()),
    path('category/<int:id>/', subcategory.SubCategoryView.as_view()),
    path('category/',category.CategoryView.as_view()),
    path('quiz/<int:id>',show_quiz.ShowQuizView.as_view()),
    path('lk/<str:user>/<int:id>/', lk_view.ShowResult.as_view(), name='return_quiz'),
    path('lk/<str:user>',lk_view.LkView.as_view()),
    path('login/',lk_view.Login.as_view()),
    path('register/',lk_view.Register.as_view())

]

