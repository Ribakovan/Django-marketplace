from django.urls import path
from core.shop.views import Home
from core.product.views import ProductDetailView, NewProductView, DeleteProduct, EditProductView, \
    Products, FavoriteProduct, FavoriteListView
from core.auth.views import SignUpView, Login, Logout, ProfileView
from core.conversation.views import NewConversation, Inbox, ConversationDetail

app_name = 'core'

urlpatterns = [
    path('', Home.as_view(), name='shop'),
    path('products/', Products.as_view(), name='products'),
    path('products/product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/product/new/', NewProductView.as_view(), name='new-product'),
    path('products/product/delete/<int:pk>/', DeleteProduct.as_view(), name='delete-product'),
    path('products/product/edit/<int:pk>/', EditProductView.as_view(), name='edit-product'),
    path('products/product/likes/', FavoriteListView.as_view(), name='favourite-list'),
    path('products/product/likes/<int:pk>/', FavoriteProduct.as_view(), name='favourite'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/conversations/', Inbox.as_view(), name='inbox'),
    path('profile/conversations/<int:pk>', ConversationDetail.as_view(), name='conversation-detail'),
    path('profile/conversations/new/<int:pk>', NewConversation.as_view(), name='new-conversation'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]
