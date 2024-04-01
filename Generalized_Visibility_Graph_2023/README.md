<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


<!-- PROJECT LOGO -->
<br />
<div align="center">


<h3 align="center">Generalized Visibility Graph For Time Series with Rotation in Polar Plane</h3>

  <p align="center">
    This repo is the implementation of our article entitled:
    <br />
    "A generalized visibility graph algorithm for analyzing biological time series having rotation in polar plane"

    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#citation">Citation</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<p align="left">    
    This repo is the implementation of our article entitled:
    <br />
    "A generalized visibility graph algorithm for analyzing biological time series having rotation in polar plane"
</p>

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Matlab]][Matlab-url]
* [![Python]][Python-url]
* [![Gephi]][Gephi-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->

### Prerequisites

You need Matlab, Gephi and Python to be installed
Matlab is for creating the visibility graphs
Gephi is for feature extraction from graphs
Python is for the machine learning

1-Matlab: https://mathworks.com
2-Python: https://python.org
3-Gephi: https://gephi.github.io

### Usage

1. There are three matlab files starting with create_vg. These files are for creating the graphs.

#create_vg_proposed.m is the proposed algorithm
#create_vg_compare.m is the compared algorithm
#create_vg_base.m is the standard algorithm

2. Matrix2GraphML.m is for converting the graph to graphml format for Gephi
3. Gephi could then be used to extract the features
4. ML_vg.py is the python code for the machine learning algorithms

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Adel Ghazikhani -  - adel.ghazi@gmail.com
Linkedin        -  - linkedin.com/in/adel-ghazikhani-93349257
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CITATION -->

##Citation

Please Cite:

Z. Ramezanpoor, A. Ghazikhani, and G. S. Bajestani, "A generalized visibility graph algorithm for analyzing biological time series having rotation in polar plane," Engineering Applications of Artificial Intelligence, vol. 128, p. 107557, 2024/02/01/ 2024.


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Matlab-url]: https://mathworks.com
[Python-url]: https://python.org
[Gephi-url]: https://gephi.github.io
