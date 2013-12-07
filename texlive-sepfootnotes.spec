# revision 28885
# category Package
# catalog-ctan /macros/latex/contrib/sepfootnotes
# catalog-date 2013-01-19 01:10:31 +0100
# catalog-license lppl1.3
# catalog-version 0.2
Name:		texlive-sepfootnotes
Version:	0.2
Release:	2
Summary:	Support footnotes and endnotes from separate files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sepfootnotes
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sepfootnotes.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sepfootnotes.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package supports footnotes and endnotes from separate
files. This is achieved with commands \sepfootnotecontent and
\sepfootnote; the former defines the content of a note, while
the latter typesets that note.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/sepfootnotes/sepfootnotes.sty
%doc %{_texmfdistdir}/doc/latex/sepfootnotes/README
%doc %{_texmfdistdir}/doc/latex/sepfootnotes/sepfootnotes.pdf
%doc %{_texmfdistdir}/doc/latex/sepfootnotes/sepfootnotes.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
