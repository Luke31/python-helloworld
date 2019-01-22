FROM frolvlad/alpine-miniconda3 as builder
RUN apk add --no-cache bash
RUN conda install conda-build
COPY .condarc /root/.condarc
COPY . /app

WORKDIR /app
RUN conda build conda.recipe

#COPY environment.yml /app/
#RUN conda env create --file app/environment.yml -p /env
#RUN source activate /env && conda install helloworld && python setup.py test

FROM frolvlad/alpine-miniconda3
MAINTAINER Lukas Schmid

EXPOSE 5000
COPY --from=builder /env /env
COPY --from=builder /app/run.py /app/run.py
WORKDIR /app
CMD source activate /env && conda install helloworld && python run.py
