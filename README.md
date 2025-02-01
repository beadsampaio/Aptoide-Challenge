# Aptoide-Challenge

## 📱 Android

De seguida estão os erros que identifiquei e as respectivas soluções aplicadas:

### 🛑 Erro 1: Entidade sem Primary Key
**Erro:**
```
error: An entity must have at least 1 field annotated with @PrimaryKey
public final class User {
```
**Explicação:**
A classe `User` foi definida como uma entidade do Room Database, mas não tinha uma chave primária. Cada entidade precisa de uma chave primária para identificação única.

**Solução:**
Identifiquei o atributo `id` como chave primária:
```
@PrimaryKey(autoGenerate = true) val id: Int = 0,
```

---
### 🛑 Erro 2: Uso do findViewById antes de setContentView
**Explicação:**
No ficheiro `MainActivity.kt`, o `findViewById` foi chamado antes de definir o layout da Activity com `setContentView(R.layout.activity_main)`, o que resultava em erro.

**Solução:**
Reorganizei o código para garantir que `setContentView` seja definido primeiro:
```
setContentView(R.layout.activity_main)

val textView = findViewById<TextView>(R.id.text_view_user)
viewModel.userName.observeForever {
    textView.text = it
}
```

---
### 🛑 Erro 3: Sem permissão de acesso à internet
**Explicação:**
A aplicação tentava aceder à internet sem a devida permissão no `AndroidManifest.xml`.

**Solução:**
Adicionei a permissão necessária:
```xml
<uses-permission android:name="android.permission.INTERNET"/>
```

---
### 🛑 Erro 4: Acesso à Base de Dados na Main Thread
**Explicação:**
A base de dados estava a ser acedida na `Main Thread`, que é responsável pela interface do utilizador. Isso poderia levar ao congelamento da interface e prejudicar a experiência de utilização.

**Solução:**
Utilizei `CoroutineScope` para realizar operações de leitura/escrita na base de dados em uma `IO thread`, mantendo a atualização da UI na `Main thread`.

**Alteração na função `loadUserData`**:
```
fun loadUserData(context: Context) {
    CoroutineScope(Dispatchers.IO).launch {
        try {
            val user = AppDatabase.getDatabase(context)?.userDao()?.getAllUsers()?.firstOrNull()
            user?.let {
                CoroutineScope(Dispatchers.Main).launch {
                    _userName.value = it.name
                    _userImage.value = it.image
                }
            }
        } catch (e: Exception) {
            e.printStackTrace()
        }
    }
}
```

---
### 🛑 Erro 5: Posts não apareciam no RecyclerView
**Explicação:**
A função `getItemCount()` estava a retornar `0`, indicando que a lista estava vazia, mesmo havendo posts.

**Solução:**
Atualizei a função para garantir que ela retorna o tamanho correto da lista de posts:
```
override fun getItemCount(): Int {
    return postList.size
}
```

## 🐍 Python

### Configuração
Para executar o projeto Python:
1. Abrir o projeto no **Visual Studio Code**.
2. No terminal, executar:
   ```sh
   pip install requests
   ```
3. Executar o script principal:
   ```sh
   python main.py
   ```
---
---

## 📱 Android  

Below are the errors I identified and the corresponding solutions applied:  

### 🛑 Error 1: Entity without Primary Key  
**Error:**  
```
error: An entity must have at least 1 field annotated with @PrimaryKey
public final class User {
```  
**Explanation:**  
The `User` class was defined as an entity in the Room Database but lacked a primary key. Each entity must have a primary key for unique identification.  

**Solution:**  
I marked the `id` attribute as the primary key:  
```
@PrimaryKey(autoGenerate = true) val id: Int = 0,
```  

---  
### 🛑 Error 2: Using findViewById before setContentView  
**Explanation:**  
In the `MainActivity.kt` file, `findViewById` was called before defining the layout with `setContentView(R.layout.activity_main)`, causing an error.  

**Solution:**  
I reorganized the code to ensure `setContentView` is defined first:  
```
setContentView(R.layout.activity_main)

val textView = findViewById<TextView>(R.id.text_view_user)
viewModel.userName.observeForever {
    textView.text = it
}
```  

---  
### 🛑 Error 3: No Internet Access Permission  
**Explanation:**  
The application attempted to access the internet without the required permission in `AndroidManifest.xml`.  

**Solution:**  
I added the necessary permission:  
```xml
<uses-permission android:name="android.permission.INTERNET"/>
```  

---  
### 🛑 Error 4: Database Access on the Main Thread  
**Explanation:**  
The database was accessed on the `Main Thread`, responsible for the user interface. This could cause UI freezing and negatively impact the user experience.  

**Solution:**  
I used `CoroutineScope` to perform database read/write operations on an `IO thread`, ensuring UI updates happen on the `Main thread`.  

**Updated `loadUserData` function:**  
```
fun loadUserData(context: Context) {
    CoroutineScope(Dispatchers.IO).launch {
        try {
            val user = AppDatabase.getDatabase(context)?.userDao()?.getAllUsers()?.firstOrNull()
            user?.let {
                CoroutineScope(Dispatchers.Main).launch {
                    _userName.value = it.name
                    _userImage.value = it.image
                }
            }
        } catch (e: Exception) {
            e.printStackTrace()
        }
    }
}
```  

---  
### 🛑 Error 5: Posts Not Displaying in RecyclerView  
**Explanation:**  
The `getItemCount()` function was returning `0`, indicating an empty list, even though there were posts available.  

**Solution:**  
I updated the function to ensure it returns the correct list size:  
```
override fun getItemCount(): Int {
    return postList.size
}
```  

## 🐍 Python  

### Setup  
To run the Python project:  
1. Open the project in **Visual Studio Code**.  
2. In the terminal, run:  
   ```sh
   pip install requests
   ```  
3. Execute the main script:  
   ```sh
   python main.py
   ```  
