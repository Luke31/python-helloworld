FROM frolvlad/alpine-miniconda3 as builder
COPY environment.yml /app/
RUN conda env create --file app/environment.yml -p /env
COPY . /app

WORKDIR /app
RUN source activate /env && tox && conda install -c conda-forge uwsgi && pip install -r requirements.txt && pip install .

FROM frolvlad/alpine-miniconda3

MAINTAINER Lukas Schmid

EXPOSE 5000
COPY --from=builder /env /env
WORKDIR /app
RUN adduser --system uwsgi
USER uwsgi
CMD source activate /env && uwsgi --http 0.0.0.0:5000 --master --module helloworld.app:APP --processes 4
