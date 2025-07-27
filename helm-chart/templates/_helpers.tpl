{{- define "todo-app.name" -}}
todo-app
{{- end }}

{{- define "todo-app.fullname" -}}
{{- printf "%s-%s" .Release.Name "app" | trunc 63 | trimSuffix "-" -}}
{{- end }}
