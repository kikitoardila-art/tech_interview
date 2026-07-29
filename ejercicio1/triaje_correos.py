import pandas as pd
import re
import os

def clasificar_correo(row):
    asunto = str(row.get('asunto', '')).lower()
    cuerpo = str(row.get('cuerpo', '')).lower()
    texto = f"{asunto} {cuerpo}"
    
    # Reglas de tipo, urgencia y asignación de responsable
    if any(k in texto for k in ['desistimiento', 'cancelar', 'devolucion', 'devolución', 'dinero']):
        tipo = 'Desistimiento / Reclamación'
        urgencia = 'ALTA'
        responsable = 'Jurídico / Cartera'
        accion = 'Revisar contrato y validar causal de desistimiento con cliente.'
    elif any(k in texto for k in ['grieta', 'humedad', 'daño', 'fuga', 'garantia', 'garantía', 'reparar']):
        tipo = 'Reclamación Técnica'
        urgencia = 'ALTA'
        responsable = 'Obras / Posventas'
        accion = 'Agendar visita técnica de inspección en inmueble.'
    elif any(k in texto for k in ['pago', 'cuota', 'saldo', 'factura', 'banco', 'crédito', 'credito']):
        tipo = 'Consulta Financiación'
        urgencia = 'MEDIA'
        responsable = 'Cartera'
        accion = 'Verificar extracto de cuenta y enviar estado de cartera.'
    elif any(k in texto for k in ['precio', 'disponibilidad', 'cotizacion', 'cotización', 'informacion', 'información', 'visita']):
        tipo = 'Consulta Comercial'
        urgencia = 'MEDIA'
        responsable = 'Ventas'
        accion = 'Enviar catálogo actualizado y agendar cita en sala de ventas.'
    else:
        tipo = 'Ambiguo / General'
        urgencia = 'BAJA'
        responsable = 'Atención al Cliente'
        accion = 'Contactar al cliente para aclarar la solicitud.'
        
    return pd.Series([tipo, urgencia, responsable, accion])

def procesar_triaje():
    ruta_csv = 'correos_clientes.csv'
    if not os.path.exists(ruta_csv):
        ruta_csv = '../correos_clientes.csv'
        
    print(f"Cargando dataset desde {ruta_csv}...")
    df = pd.read_csv(ruta_csv)
    
    # Deduplicación básica por cliente y asunto
    col_cliente = 'cliente' if 'cliente' in df.columns else ('remitente' if 'remitente' in df.columns else df.columns[0])
    col_asunto = 'asunto' if 'asunto' in df.columns else df.columns[1]
    df = df.drop_duplicates(subset=[col_cliente, col_asunto], keep='first')
    
    # Aplicar clasificación
    df[['Tipo_Peticion', 'Urgencia', 'Responsable', 'Accion_Sugerida']] = df.apply(clasificar_correo, axis=1)
    
    # Exportar resultado a Excel
    output_path = 'seguimiento_correos.xlsx'
    df.to_excel(output_path, index=False)
    print(f"✅ Procesamiento completado. Archivo generado: {output_path}")

if __name__ == '__main__':
    procesar_triaje()
