%define oname clutter-gtk

%define api 1.0
%define major 0
%define gir_major 1.0
%define libname		%mklibname %{oname} %{api} %{major}
%define girname     %mklibname %{oname}-gir %{api}
%define develname	%mklibname -d %{oname} %{api}

Summary:	GTK Support for Clutter
Name:		%{oname}3
Version:	1.0.4
Release:	2
License:	LGPLv2+
Group:		Graphics
Url:		http://clutter-project.org/
Source0:	http://www.clutter-project.org/sources/clutter-gtk/%{api}/%{oname}-%{version}.tar.xz

BuildRequires: clutter-devel >= 1.0
BuildRequires: gtk+3-devel
BuildRequires: gtk-doc
BuildRequires: docbook-dtd412-xml
BuildRequires: gobject-introspection-devel >= 0.6.3-0.20090616

%description
A library providing facilities to integrate Clutter into GTK+
applications. It provides a GTK+ widget, GtkClutterEmbed, for embedding the
default ClutterStage into any GtkContainer.

Because of limitations inside Clutter, it is only possible to embed a single
ClutterStage.

%package -n %{libname}
Summary:	GTK Support for Clutter
Group:		Graphics
Obsoletes:  %{_lib}clutter-gtk31.0_0 < 0.91.8-2

%description -n %{libname}
A library providing facilities to integrate Clutter into GTK+
applications. It provides a GTK+ widget, GtkClutterEmbed, for embedding the
default ClutterStage into any GtkContainer.

Because of limitations inside Clutter, it is only possible to embed a single
ClutterStage.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{develname}
Summary:	Development headers/libraries for %{name}
Group:		Development/X11
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Obsoletes:  %{_lib}clutter-gtk31.0-devel < 0.91.8-2

%description -n %{develname}
Development headers/libraries for %{name} (see %{libname} package)

%prep
%setup -qn %{oname}-%{version}
%apply_patches

%build
%configure2_5x \
	--disable-static \
	--enable-gtk-doc

%make

%install
rm -rf %{buildroot}
%makeinstall
find %{buildroot} -name *.la | xargs rm
%find_lang cluttergtk-%{api}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/lib%{name}-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/GtkClutter-%{api}.typelib

%files -n %{develname} -f cluttergtk-%{api}.lang
%{_libdir}/pkgconfig/%{oname}-%{api}.pc
%{_libdir}/lib%{name}-%{api}.so
%dir %{_includedir}/clutter-gtk-%{api}/%{oname}
%{_includedir}/clutter-gtk-%{api}/%{oname}/
%{_datadir}/gir-1.0/GtkClutter-%{api}.gir
%dir %{_datadir}/gtk-doc/html/%{oname}-%{api}
%doc %{_datadir}/gtk-doc/html/%{oname}-%{api}/*

