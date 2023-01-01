These are SRPM source files for an updated daemontools RPM. It is
based on the original daemontools SRPM by Matthew Hall, and has been updated
to compile and install more gracefully for RHEL and Fedora Linux.

daemontools has not been supported since 2001. The init system in
modern Linux is systemd. This package exists for curiosity and
testing, not as a system critical tool.

To build locally:

* make getsrc
* make build

To build with mock:

* make getsrc
* make

   	   Nico Kadel-Garcia
	   <nkadel@gmail.com>
