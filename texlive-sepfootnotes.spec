%global tl_name sepfootnotes
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3d
Release:	%{tl_revision}.1
Summary:	Support footnotes and endnotes from separate files
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/sepfootnotes
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sepfootnotes.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sepfootnotes.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package supports footnotes and endnotes from separate files. This is
achieved with commands \sepfootnotecontent and \sepfootnote; the former
defines the content of a note, while the latter typesets that note.

