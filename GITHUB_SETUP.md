# 🚀 Configuración de GitHub y CI/CD Pipeline

## 📋 **Paso a Paso para Activar el Pipeline**

### 1. **Crear Repositorio en GitHub**
1. Ve a [GitHub.com](https://github.com) y inicia sesión
2. Haz clic en el botón verde "New" o "+" → "New repository"
3. Nombre del repositorio: `cse270-smoke-tests` (o el nombre que prefieras)
4. Descripción: "CSE 270 Smoke Test Suite with CI/CD Pipeline"
5. **IMPORTANTE**: Deja el repositorio como **Público** (necesario para GitHub Pages)
6. **NO** inicialices con README, .gitignore, o licencia (ya los tenemos)
7. Haz clic en "Create repository"

### 2. **Conectar Repositorio Local con GitHub**
```bash
# Agregar el repositorio remoto (reemplaza TU_USUARIO con tu nombre de usuario de GitHub)
git remote add origin https://github.com/TU_USUARIO/cse270-smoke-tests.git

# Cambiar la rama principal a 'main' (estándar de GitHub)
git branch -M main

# Hacer push de todos los commits
git push -u origin main
```

### 3. **Verificar que el Pipeline se Active**
1. Ve a la pestaña "Actions" en tu repositorio de GitHub
2. Deberías ver el workflow "Simple CI/CD Pipeline for CSE 270" ejecutándose
3. El pipeline hará lo siguiente:
   - ✅ Instalar Python 3.12
   - ✅ Instalar todas las dependencias (Selenium, pytest, etc.)
   - ✅ Instalar Chrome y ChromeDriver
   - ✅ Iniciar servidor HTTP en puerto 5500
   - ✅ Ejecutar todos los smoke tests
   - ✅ Desplegar el sitio en GitHub Pages

### 4. **Monitorear la Ejecución**
- El pipeline tomará aproximadamente 5-10 minutos
- Verás logs en tiempo real de cada paso
- Si hay errores, se mostrarán en rojo
- Si todo pasa, verás ✅ verde en cada paso

## 🔧 **Solución de Problemas Comunes**

### **Error: "Chrome not found"**
- El pipeline instala Chrome automáticamente
- Si falla, verifica que el workflow tenga permisos de administrador

### **Error: "Port 5500 already in use"**
- El pipeline usa el puerto 5500 automáticamente
- No necesitas hacer nada localmente

### **Error: "Tests failed"**
- Los tests están configurados para ejecutarse en el pipeline
- Verifica que el sitio web esté funcionando correctamente

## 📊 **Verificar que Todo Funcione**

### **Localmente (Opcional)**
```bash
# Iniciar servidor local
python -m http.server 5500

# En otra terminal, ejecutar tests
python run_tests.py
```

### **En GitHub Actions**
1. Ve a Actions → "Simple CI/CD Pipeline for CSE 270"
2. Haz clic en el último commit
3. Verifica que todos los pasos tengan ✅ verde
4. Al final, ve a la pestaña "Deployments" para ver tu sitio

## 🎯 **Resultado Final**

Una vez que el pipeline se ejecute exitosamente:
- ✅ Todos los smoke tests pasarán
- ✅ El sitio se desplegará en GitHub Pages
- ✅ Tendrás un pipeline de CI/CD completamente funcional
- ✅ Los tests se ejecutarán automáticamente en cada push

## 🆘 **Si Necesitas Ayuda**

1. Revisa los logs del pipeline en GitHub Actions
2. Verifica que todos los archivos estén en el repositorio
3. Asegúrate de que el repositorio sea público
4. Contacta a tu instructor si persisten los problemas

---

**¡Tu pipeline de CI/CD está listo para funcionar! 🚀**
