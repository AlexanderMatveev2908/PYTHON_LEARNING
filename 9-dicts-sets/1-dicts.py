nested = {
    'name': 'John',
    'address': {
        'street': {
            'nr': 34,
            'name': 'Wayland'
        }
    }
}

print(nested['address']['street']['nr'])
print((nested.get('address', {})).get('street', {}).get('nrb', None))

