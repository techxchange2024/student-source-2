FROM icr.io/appcafe/websphere-traditional:9.0.5.15
COPY --chown=was:root ./target/modresorts-2.0.0.war /work/app/
COPY --chown=was:root ./target/was-deploy.py ./target/was-datasource-create.py ./target/was-connectionfactory-create.py /work/config/
COPY --chown=was:root ./db-drivers/* /db-drivers/
RUN /work/configure.sh