-- this file was manually created
INSERT INTO public.users (display_name, email,handle, cognito_user_id)
VALUES
  ('Andrew Brown', 'dahurdayo@gmail.com', 'andrewbrown' ,'MOCK'),
  ('Andrew Bayko', 'ekene@gmail.com', 'bayko' ,'MOCK');

INSERT INTO public.activities (user_uuid, message, expires_at)
VALUES
  (
    (SELECT uuid FROM public.users WHERE handle = 'andrewbrown' LIMIT 1),
    'This was imported as seed data!',
    current_timestamp + interval '10 day'
  );
