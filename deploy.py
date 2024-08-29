import argparse
import logging
from truefoundry.deploy import Service, Build, DockerFileBuild, PythonBuild, Port, Resources

logging.basicConfig(level=logging.INFO)

service = Service(
  name="load-testing",

  # --- Build configuration i.e. How to package and build source code ---
  # This will instruct TrueFoundry to automatically generate the Dockerfile and build it
  image=Build(
    build_spec=DockerFileBuild(
      dockerfile_path="./Dockerfile",
    )
    # You can use PythonBuild or DockerFileBuild for build spec like follows:
    # build_spec=PythonBuild() or build_spec=DockerFileBuild()
  ),
  # Alternatively, you can use an already built public image of this codebase like follows:
  # image=Image(image_uri="truefoundrycloud/emotion-classification-fastapi:0.0.1")

  # --- Endpoints configuration i.e. How requests will reach the container ---
  ports=[
    Port(
      port=8089,
      host="load-testing-ishaan-ws-8089.tfy-ctl-euwe1-devtest.devtest.truefoundry.tech",
    )
  ],

  # --- Environment Variables ---
  env={},

  # --- Resources ---
  resources=Resources(
    cpu_request=0.5, cpu_limit=0.5,
    memory_request=1000, memory_limit=1000,
    ephemeral_storage_request=500, ephemeral_storage_limit=500
  ),
)

# Get your workspace fqn from https://docs.truefoundry.com/docs/workspace#copy-workspace-fqn-fully-qualified-name
service.deploy(workspace_fqn="tfy-ctl-euwe1-devtest:ishaan-ws")