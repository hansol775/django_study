from django.contrib import admin
from .models import Post
from django.utils.safestring import mark_safe



# 장고 모델을 어드민에 적용하는 방법 3가지

# 첫번째 방법
# admin.site.register(Post) 


# 두번째 방법 
@admin.register(Post) # Wrapping
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo_tag', 'message', 'created_at', 'updated_at', 'message_length', 'is_public']
    list_display_links = ['id', 'message'] # 링크주는거 여러개 가능 ㅋㅋ
    list_filter = ['created_at', 'is_public']
    search_fields = ['message']

    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" style="width: 72px;" />')
        return None
    
    def message_length(self, post):
        # return len(post.message)
        return f"{len(post.message)}글자"


# 세번째 방법
# class PostAdmin(admin.ModelAdmin):
#     pass

# admin.site.register(Post, PostAdmin)