lib-blockchain-btc-address-gen
==============================

A library for generating Bitcoin Public and Private keys in unison using Blockchain.info 's wallet generator.

##Usage

* Import the library with `import libbcbtcag`.
* Return the new public key and private key ij one string seperated by a space with `generate(True)`.
* Use `generate(False)` for `http` (**unsecure**) and use `generate(True)` for `https` (**secure**).
