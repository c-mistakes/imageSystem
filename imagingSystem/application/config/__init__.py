from datetime import datetime, timedelta, timezone

# Define UTC offset for Beijing time (+8 hours)
utc_offset = timedelta(hours=8)

# Create a naive datetime object for the desired date and time in UTC
# utc_time = datetime(2024, 10, 11, 0, 0, 0).replace(tzinfo=timezone.utc)
utc_time = datetime(2024, 11, 11, 0, 0, 0)


# Convert UTC time to Beijing time
end_day = utc_time

image_suffixes = ['.png', '.jpg', '.jpeg', '.tif', '.tiff', '.bmp']