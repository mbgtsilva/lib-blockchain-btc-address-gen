lib-blockchain-btc-address-gen [![Build Status](https://travis-ci.org/deavmi/lib-blockchain-btc-address-gen.svg?branch=master)](https://travis-ci.org/deavmi/lib-blockchain-btc-address-gen)
==============================



A library for generating Bitcoin Public and Private keys in unison using Blockchain.info 's wallet generator.

##Usage

* Import the library with `import libbcbtcag`.
* Return the new public key and private key ij one string seperated by a space with `generate(True)`.
* Use `generate(False)` for `http` (**unsecure**) and use `generate(True)` for `https` (**secure**).

##Helpful links

* [BitcoinTalk Release](https://bitcointalk.org/index.php?topic=869172.0)

<hr>

![GPL 3 Logo](http://www.gnu.org/graphics/gplv3-127x51.png)

This software is licensed under the GNU General Public License version three or above.

**Crowbar 2015.**
