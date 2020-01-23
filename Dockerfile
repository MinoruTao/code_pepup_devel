FROM lambci/lambda:python3.7

ENV AWS_DEFAULT_REGION us-west-2
ENV APP_DIR /var/task

ADD . .

CMD pip install selenium -t $APP_DIR

#RUN python pepup_login.py '{"Hello":"World"}'
RUN ls -l
#RUN cat hello.txt
