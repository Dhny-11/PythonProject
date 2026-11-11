def verify_card_number(card_number):
    clean_number = card_number.replace('-', '').replace(' ', '')
    
    digits = [int(d) for d in str(clean_number)][::-1]
    
    total_sum = 0
    
    for i, digit in enumerate(digits):
        if i % 2 == 1:
            doubled = digit * 2
            if doubled > 9:
                doubled -= 9
            total_sum += doubled
        else:
            total_sum += digit
    if total_sum % 10 == 0:
        return 'VALID!'
    else:
        return 'INVALID!'