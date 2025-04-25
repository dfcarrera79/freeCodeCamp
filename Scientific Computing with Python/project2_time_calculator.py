## Build a Time Calculator Project

def add_time(start_time, duration, start_day=None):
    # Parse the start time
    start_time_parts = start_time.split()
    time_part = start_time_parts[0]
    period = start_time_parts[1]
    
    # Split hours and minutes
    hours, minutes = map(int, time_part.split(':'))
    
    # Convert to 24-hour format for easier calculation
    if period == 'PM' and hours != 12:
        hours += 12
    elif period == 'AM' and hours == 12:
        hours = 0
    
    # Parse the duration
    duration_hours, duration_minutes = map(int, duration.split(':'))
    
    # Add duration to start time
    total_minutes = minutes + duration_minutes
    added_hours = total_minutes // 60
    remaining_minutes = total_minutes % 60
    
    total_hours = hours + duration_hours + added_hours
    added_days = total_hours // 24
    remaining_hours = total_hours % 24
    
    # Convert back to 12-hour format
    if remaining_hours == 0:
        new_period = 'AM'
        new_hour = 12
    elif remaining_hours < 12:
        new_period = 'AM'
        new_hour = remaining_hours
    elif remaining_hours == 12:
        new_period = 'PM'
        new_hour = 12
    else:
        new_period = 'PM'
        new_hour = remaining_hours - 12
    
    # Format the new time
    new_time = f"{new_hour}:{remaining_minutes:02d} {new_period}"
    
    # Handle day of the week if provided
    if start_day:
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        start_day_lower = start_day.lower()
        
        # Find the index of the starting day
        day_index = None
        for i, day in enumerate(days_of_week):
            if day.lower() == start_day_lower:
                day_index = i
                break
        
        if day_index is not None:
            new_day_index = (day_index + added_days) % 7
            new_day = days_of_week[new_day_index]
            new_time += f", {new_day}"
    
    # Handle day difference information
    if added_days == 1:
        new_time += " (next day)"
    elif added_days > 1:
        new_time += f" ({added_days} days later)"
    
    return new_time