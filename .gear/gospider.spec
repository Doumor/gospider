%global import_path github.com/jaeles-project/gospider

Name:    gospider
Version: 1.1.6
Release: alt1

Summary: Fast web spider written in Go
License: MIT
Group:   Other
Url:     https://github.com/jaeles-project/gospider

Source: %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang /proc
BuildArch: %go_arches

%description
GoSpider - Fast web spider written in Go
Features
 * Fast web crawling
 * Brute force and parse sitemap.xml
 * Parse robots.txt
 * Generate and verify link from JavaScript files
 * Link Finder
 * Find AWS-S3 from response source
 * Find subdomains from response source
 * Get URLs from Wayback Machine, Common Crawl, Virus Total, Alien Vault
 * Format output easy to Grep
 * Support Burp input
 * Crawl multiple sites in parallel
 * Random mobile/web User-Agent


%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc *.md LICENSE
%_bindir/gospider

%changelog
* Tue Sep 19 2023 Danilkin Danila <danild@altlinux.org> 1.1.6-alt1
- Initial build for Sisyphus
