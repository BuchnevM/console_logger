*Inspired by the original __logging__ package from Python.*

## About this package

*Console logger* is a simple logging package for Python. The main feature of the package is an ability to log messages in different ways. 
Log records can be output as follows:

- console output; 
- output to a file; 
- both console and file output.

## Supported features

- easy access to logger at module level
- logging record can be emitted with specified keywords without logger changing
- colored output in console
- rotating text files when the current file reaches a certain size

## Usage

### How to install

```commandline
pip install console_logger
```

### How to use

1. Import the package.

   ```python
   import console_logger
    ```

2. Create a logger instance...

   ```python
   my_logger = console_logger.Logger()
    ```
   
3. ... and use it for logging messages.
   
   ```python
   my_logger.info("My message with severity 'INFO'.")
   ```

### Examples

```pycon
>>> import console_logger
>>> my_logger = console_logger.Logger()
>>> my_logger.info('Here we go!')
08.09.22 00:01:55.123 [  INFO  ] Here we go!
>>> my_logger.debug('This message will not be displayed')
>>> my_logger.error('Oops!')
08.09.22 00:01:57.456 [ ERROR  ] Oops!
```