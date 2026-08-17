# Basic Usage

Always prioritize using a supported framework over using the generated SDK
directly. Supported frameworks simplify the developer experience and help ensure
best practices are followed.





## Advanced Usage
If a user is not using a supported framework, they can use the generated SDK directly.

Here's an example of how to use it with the first 5 operations:

```js
import { lihatSemuaUser, addNewUser } from '@dataconnect/generated';


// Operation LihatSemuaUser: 
const { data } = await LihatSemuaUser(dataConnect);

// Operation addNewUser:  For variables, look at type AddNewUserVars in ../index.d.ts
const { data } = await AddNewUser(dataConnect, addNewUserVars);


```