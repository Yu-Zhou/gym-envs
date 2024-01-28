from setuptools import setup

setup(
    name='gym_envs',
    version='0.0.3',
    description='Gym envs - useful for conducting RL experiments',
    url='https://github.com/Yu-Zhou/gym-envs',
    author='Isabella Zhou',
    author_email='isabella910207@gmail.com',
    packages=['gym_envs', 'gym_envs.envs'],
    license='MIT License',
    install_requires=['gym==0.26.2','six==1.16.0'],
)
