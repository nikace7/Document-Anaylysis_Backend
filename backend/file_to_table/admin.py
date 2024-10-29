from django.contrib import admin
from .models import (
    User,
    VerificationEmail,
    FileInput,
    FilePage,
    ImageInput,
    WordConversion,
    ScannedFile,
    ScannedImage,
    GuestScannedFile,
    GuestScannedImage,
    PasswordResetRequest,
    BugReport,
    BugImage,
    ContactForm,
    ExtractedText
)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'contact', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'contact')
    list_filter = ('is_staff', 'is_active')

@admin.register(VerificationEmail)
class VerificationEmailAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_on', 'status')
    search_fields = ('user__email',)
    list_filter = ('status',)

@admin.register(FileInput)
class FileInputAdmin(admin.ModelAdmin):
    list_display = ('user', 'file', 'created')
    search_fields = ('user__email',)
    list_filter = ('created',)

@admin.register(FilePage)
class FilePageAdmin(admin.ModelAdmin):
    list_display = ('file', 'created')
    search_fields = ('file__file',)

@admin.register(ImageInput)
class ImageInputAdmin(admin.ModelAdmin):
    list_display = ('user', 'image', 'created')
    search_fields = ('user__email',)

@admin.register(WordConversion)
class WordConversionAdmin(admin.ModelAdmin):
    list_display = ('user', 'created', 'image', 'document')
    search_fields = ('user__email',)

@admin.register(ScannedFile)
class ScannedFileAdmin(admin.ModelAdmin):
    list_display = ('user', 'file', 'created')
    search_fields = ('user__email',)

@admin.register(ScannedImage)
class ScannedImageAdmin(admin.ModelAdmin):
    list_display = ('file', 'created')
    search_fields = ('file__file',)

@admin.register(GuestScannedFile)
class GuestScannedFileAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'file', 'created')
    search_fields = ('identifier',)

@admin.register(GuestScannedImage)
class GuestScannedImageAdmin(admin.ModelAdmin):
    list_display = ('file', 'created')
    search_fields = ('file__file',)

@admin.register(PasswordResetRequest)
class PasswordResetRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'created', 'is_active', 'code')
    search_fields = ('user__email',)

@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('user', 'description')
    search_fields = ('user__email', 'description')

@admin.register(BugImage)
class BugImageAdmin(admin.ModelAdmin):
    list_display = ('report', 'image')
    search_fields = ('report__description',)

@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'description')
    search_fields = ('name', 'email', 'subject')

@admin.register(ExtractedText)
class ExtractedTextAdmin(admin.ModelAdmin):
    list_display = ('user', 'created', 'image', 'extracted_text_preview')
    search_fields = ('user__username', 'extracted_text')
    list_filter = ('user', 'created')
    ordering = ('-created',)

    def extracted_text_preview(self, obj):
        return obj.extracted_text[:50] if obj.extracted_text else 'No text extracted'
    
    extracted_text_preview.short_description = 'Extracted Text Preview'