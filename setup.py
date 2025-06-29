from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="callback-error-plugin-demo-7",  # make sure the package name is unique on PyPi
    version="0.0.1",
    install_requires=[
        "dash>=3.0.3",
    ],
    python_requires=">=3.8",
    entry_points={"dash_hooks": ["callback_error_plugin_demo_7 = callback_error_plugin_demo_7"]},
    packages=["callback_error_plugin_demo_7"],
    author="koveszter",
    description="A plugin to print Dash app errors on the header section of the page",
    long_description=long_description,  # Now this is the actual README content
    long_description_content_type="text/markdown",  # If using Markdown for README
    url="https://github.com/banana0000/Hook-test",  # Add link to your repo/homepage
    license="MIT",  # Or your chosen license (e.g., Apache-2.0, BSD-3-Clause)
    classifiers=[
        "Development Status :: 3 - Alpha",  # Or Beta, Production/Stable
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Framework :: Dash",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",  # Match your license
        "Operating System :: OS Independent",
    ],
)
