FROM debian
RUN echo 'deb http://mirror.kku.ac.th/debian/ stable main contrib non-free' > /etc/apt/sources.list
RUN echo 'deb http://mirrors.psu.ac.th/debian/ stable main contrib non-free' >> /etc/apt/sources.list

RUN apt update --fix-missing && apt dist-upgrade -y
RUN apt install -y python3 python3-dev python3-pip 
 
COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
 
EXPOSE 8000
CMD ["python3", "chat_bot/manage.py", "runserver", "0.0.0.0:8000"]
