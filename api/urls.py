from django.urls import path
from api.views import category_views, todo_views, groups_views


urlpatterns = [
    path('category/create_category', category_views.CreateCategoryView.as_view()),
    path('category/delete_category_by_id/<int:pk>/', category_views.DeleteCategoryByIdView.as_view()),
    path('category/update_category_by_id/<int:pk>/', category_views.UpdateCategoryByIdView.as_view()),
    path('category/find_all_categories/', category_views.GetCategoryView.as_view()),
    path('category/find_category_by_id/<int:pl>/', category_views.FindCategoryByIdView.as_view()),
    path('todo/create_todo', todo_views.CreateTodoViews.as_view()),
    path('todo/delete_todo_by_id/<int:pk>/', todo_views.DeleteTodoViews.as_view()),
    path('todo/update_todo_by_id/<int:pk>/', todo_views.UpdateTodoViews.as_view()),
    path('todo/find_all_todos/', todo_views.GetTodoViews.as_view()),
    # GROUPS
    path("group/create_group/", groups_views.CreateGroupView.as_view()),
    path("group/delete_group_by_id/<int:pk>/", groups_views.DeleteGroupByIdView.as_view()),
    path("group/update_group_by_id/<int:pk>/", groups_views.UpdateGroupByIdView.as_view()),
    path("group/find_all_groups/",groups_views.GetGroupView.as_view()),
    path("group/find_group_by_id/<int:pk>/",groups_views.FindGroupByIdView.as_view()),

]