# revision 25574
# category Package
# catalog-ctan /macros/latex/contrib/sepfootnotes
# catalog-date 2012-03-06 12:02:15 +0100
# catalog-license lppl1.3
# catalog-version 0.1
Name:		texlive-sepfootnotes
Version:	0.1
Release:	3
Summary:	Define the texts of footnotes defined before their marks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sepfootnotes
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sepfootnotes.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sepfootnotes.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sepfootnotes.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows the content of footnotes to be defined
before their marks are inserted in a document. In this way,
footnotes and endnotes can easily be grouped together in a
separate file, so that the main body is less cluttered.

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
#- source
%doc %{_texmfdistdir}/source/latex/sepfootnotes/sepfootnotes.dtx
%doc %{_texmfdistdir}/source/latex/sepfootnotes/sepfootnotes.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Fri Mar 09 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.1-2
+ Revision: 783481
- rebuild without scriptlet dependencies

* Wed Mar 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1-1
+ Revision: 783077
- Import texlive-sepfootnotes
- Import texlive-sepfootnotes

