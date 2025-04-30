import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable track modifications to save memory
    # UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
    # ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    # MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Limit upload size to 16 MB
    # IMAGE_SIZE = (800, 800)  # Resize images to this size
    # IMAGE_QUALITY = 85  # JPEG quality for saving images
    # IMAGE_FORMAT = 'JPEG'  # Format to save images
    # THUMBNAIL_SIZE = (150, 150)  # Size for thumbnail images
    # THUMBNAIL_QUALITY = 80  # JPEG quality for thumbnail images
    # THUMBNAIL_FORMAT = 'JPEG'  # Format to save thumbnail images
    # IMAGE_CACHE_DIR = os.path.join(UPLOAD_FOLDER, 'cache')  # Directory for cached images
    # THUMBNAIL_CACHE_DIR = os.path.join(UPLOAD_FOLDER, 'thumbnails')  # Directory for cached thumbnails
    # CACHE_TIMEOUT = 60 * 60 * 24  # Cache timeout in seconds (1 day)
    # CACHE_DIR = os.path.join(UPLOAD_FOLDER, 'cache')  # Directory for cached images
    # CACHE_SIZE = 100 * 1024 * 1024  # Cache size limit in bytes (100 MB)
    # CACHE_TYPE = 'filesystem'  # Use filesystem cache
    # CACHE_THRESHOLD = 100  # Number of items to keep in cache
    # CACHE_DEFAULT_TIMEOUT = 60 * 60  # Default timeout for cache items (1 hour)
