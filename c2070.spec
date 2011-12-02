Name:           c2070
Version:        0.99
Release:        7%{?dist}
Summary:        Converts bitcmyk data to Lexmark 2070 printer language

Group:          System Environment/Libraries
License:        GPL+
# This is the original one, but has gone away...
#URL:            http://www.kornblum.i-p.com/2070/Lexmark2070.html
# ...and as the original upstream author did not respond to e-mails,
# here is at least some reference:
URL:            http://www.linuxprinting.org/show_driver.cgi?driver=%{name}
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
This is a filter to convert bitcmyk data such as produced by ghostscript to
the printer language of Lexmark 2070 printers.  It is meant to be used
by the PostScript Description files of the drivers from the foomatic package.

%prep
%setup -q

%build
# The included Makefile is badly written
%{__cc} %{optflags} -o c2070 c2070.c

%install
rm -rf $RPM_BUILD_ROOT
%{__mkdir} -p $RPM_BUILD_ROOT/%{_bindir}
%{__install} c2070 $RPM_BUILD_ROOT/%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/c2070
%doc LICENSE README

%changelog
* Thu Mar  4 2010 Tim Waugh <twaugh@redhat.com> - 0.99-7
- Ship LICENSE file.

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.99-6.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.99-4
- Autorebuild for GCC 4.3

* Tue Sep 18 2007 Lubomir Kundrak <lkundrak@redhat.com> 0.99-3
- The source for the package had died away

* Fri Aug 3 2007 Lubomir Kundrak <lkundrak@redhat.com> 0.99-2
- Modify the License tag in accordance with the new guidelines

* Thu Jun 7 2007 Lubomir Kundrak <lkundrak@redhat.com> 0.99-1
- Initial package
