% Generated by roxygen2: do not edit by hand
% Please edit documentation in R/ee_check.R
\name{ee_check-tools}
\alias{ee_check-tools}
\alias{ee_check}
\alias{ee_check_python}
\alias{ee_check_rgee_python_packages}
\alias{ee_check_credentials}
\title{Interface to check Python and non-R rgee dependencies}
\usage{
ee_check()

ee_check_python(quiet = FALSE)

ee_check_rgee_python_packages(quiet = FALSE)

ee_check_credentials()
}
\arguments{
\item{quiet}{logical. Suppress info message}
}
\description{
R functions for checking sanity of Third-Party Python
packages and credentials.
}
\examples{
\dontrun{
library(rgee)
ee_reattach() # reattach ee as a reserved word
ee_check_python()
ee_check_rgee_python_packages()
ee_check_credentials()
ee_check() # put it all together
}
}
