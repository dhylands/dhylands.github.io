---
layout: post
title: Generating rustdoc for github pages (Drone OS)
tags:
- DroneOS
- Rust
---

I've been playing with [DroneOS](https://drone-os.com) and created a crate with some
utility functions for the STM32F4xx series of processors. Unfortunately, the way that
Drone OS builds, you can't call cargo doc directly. It needs to be invoked from
the `drone` program, which means that I couldn't take advantage of [Docs.rs](https://docs.rs).

This blog post describes what I needed to do to get a second github pages site setup
and have travis generate the documentation for me.

This blog (https://blog.davehylands.com) is currently hosted as a github pages
[repository](https://github.com/dhylands/dhylands.github.io).

My crate is found in this [repository](https://github.com/dhylands/dh-drone-stm32f4-utils).

Step 1 - Goto your domain name service provider and add a CNAME DNS entry which redirects
dh-drone-stm32f4-utils.davehylands.com to dhylands.github.io. Now I have both blog.davehylands.com
and dh-drone-stm32f4-utils.davehylands.com both redirecting to dhylands.github.io.

I put this as the first step since it takes a few minutes for this to filter through through the DNS
servers.

Step 2 - Generate a github acces token [here](https://github.com/settings/tokens). Make sure
you record the token before closing the window, since you won't be able to retrieve/view it
once the window is closed.

Step 3 - [Activate your repository](https://docs.travis-ci.com/user/tutorial/#to-get-started-with-travis-ci-using-github) on travis.

Step 4 - Goto your travis repository (mine was https://travis-ci.org/github/dhylands/dh-drone-stm32f4-utils)
and click on More Options -> Settings (or add settings to your repository URL). Add an environment
variable called GITHIB_TOKEN and paste in the value from Step 2 in. I also set
"Only available on the master branch" and made sure "Display Value in build log" is NOT set.

Step 5 - Create your .travis.yml file. Mine looks like this:
```
language: rust
rust:
- stable
cache: cargo
before_install:
- cargo +stable install just
- cat rust-toolchain
- rustup install $(cat rust-toolchain)
- rustup toolchain install $(cat rust-toolchain) -c rust-src -c llvm-tools-preview -t thumbv7em-none-eabihf
- cargo +$(cat rust-toolchain) install drone
script:
- just doc
- echo dh-drone-stm32f4-utils.davehylands.com > target/thumbv7em-none-eabihf/doc/CNAME
- cp index.html target/thumbv7em-none-eabihf/doc
deploy:
  local_dir: target/thumbv7em-none-eabihf/doc
  provider: pages
  skip_cleanup: true
  github_token: "$GITHUB_TOKEN"
  keep_history: true
  on:
    branch: master
```
The `before_install:` section installs `just` using the stable version of the rust toolchain. Then it installs
the appropriate nightly toolchain and the required dependencies needs for cargo doc to work. Finally it
installs the drone CLI tool.

The `script:` uses the `just doc` command to build the actual documentation. The generated documnetation
(for the STM32F4xx) winds up in the target tree: `target/thumbv7em-none-eabihf/doc`. This directory tree
will wind up getting checked into the `gh-pages` branch of your repository. We need to create a text file
called CNAME which matches the CNAME entry that was created in Step 1. `cargo doc` crates the crate
documentation in a directory with the `name` from your Cargo.toml file, but with dashes replaced by
underscores.
I generated a redirection HTML file using
[this online generator](http://insider.zone/tools/client-side-url-redirect-generator/). This way when
the user browses your custom URL (dh-drone-stm32f4-utils.davehylands.com) then it will redirect the user
into the appropriate subdirectory.

The `deploy:` section tells travis to put the generated HTML files into the gh-pages branch of your repository
(this is where the token generated in step 2 is used).

Step 6 - Verify that GitHub Pages is setup. Goto the Settings for your github repository and scroll down
to the github pages section. Ensure that the pages is set to use the gh-pages branch, and that the Custom
domain is filled in.

Step 7 - Push your changes to github (adding the .travis.yml and the generated index.html file). This should trigger travis to build the documentation.

If you can ping your custom URL (http://dh-drone-stm32f4-utils.davehylands.com) and get back an IP address
then you know that the DNS changes have been propogated. You should then be able to browse to that URL and
see your generated documentation.
