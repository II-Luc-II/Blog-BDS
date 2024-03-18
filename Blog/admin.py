from django.contrib import admin
from Blog.models import Category, Comment, Post, Profile, Tag, Contact
from django.utils.html import format_html
from django.urls import reverse


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'display_title', 'author', 'category', 'is_published', 'created_at',
                    'updated_at', 'display_actions')
    list_filter = ('is_published', 'category', 'tags')
    list_editable = ('is_published',)
    list_per_page = 15
    list_max_show_all = 100
    search_fields = ('title', 'content')

    def display_title(self, post):
        no_icon = '<img src="/public/admin/img/icon-no.svg" alt="False">'
        yes_icon = '<img src="/public/admin/img/icon-yes.svg" alt="True">'

        if post.is_published:
            title = '<span style="color:gray"> &nbsp;' + post.title + '<span>'
            return format_html(yes_icon + title)
        else:
            title = '<span style="color:red"> &nbsp;' + post.title + '<span>'
            return format_html(no_icon + title)

    def display_actions(self, post):
        return format_html(
            '<a href="{}" class="addLink">View</a> &nbsp;'
            '<a href="{}" class="addLink">Edit</a> &nbsp;'
            '<a href="{}" class="addLink">Delete</a> &nbsp;',
            reverse('admin:Blog_post_change', args=[post.id]),
            reverse('admin:Blog_post_change', args=[post.id]),
            reverse('admin:Blog_post_delete', args=[post.id])
            )

    display_actions.short_description = 'Action'
    display_title.short_description = 'Title'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    list_per_page = 15
    list_max_show_all = 100
    search_fields = ('name', 'description')


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    list_per_page = 15
    list_max_show_all = 100
    search_fields = ('name', 'description')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'user', 'created_at', 'updated_at')
    list_filter = ('user', 'created_at', 'updated_at')
    list_per_page = 15
    list_max_show_all = 100
    search_fields = ('user', 'updated_at')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject', 'file', 'created_at')
    list_filter = ('name', 'email', 'subject')
    list_editable = ('email',)
    list_per_page = 15
    list_max_show_all = 100
    search_fields = ('name', 'email', 'subject')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'post', 'note', 'created_at', 'updated_at', 'content')
    list_filter = ('author', 'post', 'note', 'created_at')
    list_per_page = 15
    list_max_show_all = 100
    search_fields = ('author', 'post', 'note', 'created_at')


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Contact, ContactAdmin)

