Codeforces API package documentation
====================================

.. warning::
   This is a WIP work.

Codeforces is a website that hosts competitive programming contests. This
project acts as a bridge between its API and your code, giving you the tools to
retrieve data from it.

The primary objective of this package is to give the programmer the facility of
usage that this API needs. Also the integration with the language was a main
concern when developing it, so you can expect typed methods and data efficient
data classes (using python's
`__slots__ property <https://wiki.python.org/moin/UsingSlots>`_)

Basic Usage
-----------

The usage is pretty straightforward:


.. literalinclude:: examples/user_info.py
   :caption: Example of
        `user.info <https://codeforces.com/apiHelp/methods#user.info>`_
        API method.
   :language: python

You just need to instantiate a :class:`Client` object (the one making the API
requests). and then you can start using it within an `async with` expression.

The :class:`Client` object has built-in methods for every Codeforces API
endpoint, but in `snake_case` instead of Codeforces's `pascalCase` and
replacing every dot with an underscore. For example, the api method
`blogEntry.comments <https://codeforces.com/apiHelp/methods#blogEntry.comments>`_
is the equivalent of
:meth:`~cforces.methods.blog_entry.BlogEntry.blog_entry_comments` inside the
object.

Authentication
--------------

The Codeforces API allows user authentication via the usage of an api key
and secret pair. Those credentials are obtained in the settings panel of your
Codeforces account, in the "API" section. As an alternative, you can directly
access it from `this link <https://codeforces.com/settings/api>`_.

This pair is used in the client for authenticating itself. It is supplied using
the method :meth:`~cforces.Client.auth`:

.. literalinclude:: examples/user_friends.py
   :caption: Example of
        `user.friends <https://codeforces.com/apiHelp/methods#user.info>`_
        API method with an authenticated user.
   :language: python


.. toctree::
   :maxdepth: 4
   :caption: Contents:

   Enumerations <enums/index>
   Errors <errors/index>
   Methods <methods/index>
   Types <types/index>
