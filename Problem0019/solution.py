
months = [
	31, # Jan
	28, # Feb
	31, # Mar
	30, # Apr
	31, # May
	30, # Jun
	31, # Jul
	31, # Aug
	30, # Sep
	31, # Oct
	30, # Nov
	31, # Dec
]

def solution(start, end):
	total_sundays = 0
	current_day = 0
	for year in range(1900, 2001):
		count_year = year >= start and year < end
		for month in range(0, 12):
			days = months[month]
			if is_leap_year(year) and month == 1:
				days += 1
			for day in range(0, days):
				if day == 1 and current_day == 6 and count_year:
					total_sundays += 1
				current_day+=1
				if current_day == 7:
					current_day = 0
	print(total_sundays)

def is_leap_year(year):
	if year % 4 != 0:
		return False
	elif year % 100 != 0:
		return True
	elif year % 400 != 0:
		return False
	else:
		return True
	
if __name__ == '__main__':
	solution(1901, 2001)