import json
import psycopg2
import os

def lambda_handler(event, context):
    user = event['request']['userAttributes']
    print('userAttributes')
    print(user)

    user_display_name = user.get('name')
    user_email = user.get('email')
    user_handle = user.get('preferred_username')
    user_cognito_id = user.get('sub')

    # Debug print statements to ensure values are extracted correctly
    print(f'user_display_name: {user_display_name}')
    print(f'user_email: {user_email}')
    print(f'user_handle: {user_handle}')
    print(f'user_cognito_id: {user_cognito_id}')

    conn = None
    try:
        print('entered-try')
        sql = """
            INSERT INTO public.users (
                display_name, 
                email,
                handle, 
                cognito_user_id
            ) 
            VALUES (%s, %s, %s, %s)
        """
        print('SQL Statement ----')
        print(sql)
        
        # Check the connection URL
        conn_url = os.getenv('CONNECTION_URL')
        print(f'Connection URL: {conn_url}')
        
        conn = psycopg2.connect(conn_url)
        cur = conn.cursor()
        
        params = [
            user_display_name,
            user_email,
            user_handle,
            user_cognito_id
        ]
        
        print('Executing SQL statement with parameters:')
        print(params)
        
        cur.execute(sql, params)
        conn.commit()
        print('Data committed to the database.')
        
    except (Exception, psycopg2.DatabaseError) as error:
        print('Error occurred:')
        print(error)
    finally:
        if conn is not None:
            cur.close()
            conn.close()
            print('Database connection closed.')

    return event
