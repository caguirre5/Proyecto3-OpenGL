vertex_shader = '''
#version 450 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texcoords;
layout (location = 2) in vec3 normals;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

uniform float time;

out vec2 UVs;
out vec3 norms;
out vec3 pos;

void main()
{
    UVs = texcoords;
    norms = normals;
    pos = (modelMatrix * vec4(position + normals * sin(time * 3)/10, 1.0)).xyz;
                                                              //vec4(position + normals * sin(time * 3)/10
    gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(position, 1.0);

}
'''

vertex_shader_expand = '''
#version 450 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texcoords;
layout (location = 2) in vec3 normals;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

uniform float time;

out vec2 UVs;
out vec3 norms;
out vec3 pos;

void main()
{
    UVs = texcoords;
    norms = normals;
    pos = (modelMatrix * vec4(position + normals * sin(time * 3)/10, 1.0)).xyz;
                                                              //vec4(position + normals * sin(time * 3)/10
    gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(position + normals/10, 1.0);

}
'''

vertex_shader_expandloop = '''
#version 450 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texcoords;
layout (location = 2) in vec3 normals;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

uniform float time;

out vec2 UVs;
out vec3 norms;
out vec3 pos;

void main()
{
    UVs = texcoords;
    norms = normals;
    pos = (modelMatrix * vec4(position + normals * sin(time * 3)/10, 1.0)).xyz;
                                                              //vec4(position + normals * sin+1(time * 3)/30
    gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(position + normals * (-sin(time * 3)+1)/30, 1.0);

}
'''

fragment_shader = '''
#version 450 core

out vec4 fragColor;

in vec2 UVs;
in vec3 norms;
in vec3 pos;

uniform vec3 pointLight;

uniform sampler2D tex;

void main()
{
    float intensity = dot(norms, normalize(pointLight - pos));
    fragColor = texture(tex, UVs) * intensity;
}
'''

fragment_shader_toon = '''
#version 450 core

out vec4 fragColor;

in vec2 UVs;
in vec3 norms;
in vec3 pos;

uniform vec3 pointLight;

uniform sampler2D tex;

void main()
{
    float intensity = dot(norms, normalize(pointLight - pos));
    if (intensity < 0.2) {
        intensity = 0.1;
    } else if (intensity < 0.5){
        intensity = 0.4;
    } else if (intensity < 0.8){
        intensity = 0.7;
    } else {
        intensity = 1;
    }
    fragColor = texture(tex, UVs) * intensity;
}
'''

fragment_shader_termal = '''
#version 450 core

out vec4 fragColor;

in vec2 UVs;
in vec3 norms;
in vec3 pos;

uniform vec3 pointLight;

uniform sampler2D tex;

void main()
{
    float intensity = dot(norms, normalize(pointLight - pos));
    if (intensity < 0.2) {
        fragColor = vec4(0,0,1, 1.0);
    } else if (intensity < 0.5){
        fragColor = vec4(0,1,1, 1.0);
    } else if (intensity < 0.8){
        fragColor = vec4(1,1,0, 1.0);
    } else {
        fragColor = vec4(1,0,0, 1.0);
    }
}
'''

fragment_shader_rainbow = '''
#version 450 core

out vec4 fragColor;

in vec2 UVs;
in vec3 norms;
in vec3 pos;

uniform vec3 pointLight;
uniform float time;
uniform sampler2D tex;

void main()
{
    float intensity = dot(norms, normalize(pointLight - pos));
    fragColor = texture(tex, UVs) * vec4((1 + 1*sin(time * 5)),(1 - 1*sin(time * 10)),(1 + 1*sin(time * 15)),1.0) * intensity;
}
'''

fragment_shader_bluered = '''
#version 450 core

out vec4 fragColor;

in vec2 UVs;
in vec3 norms;
in vec3 pos;

uniform vec3 pointLight;
uniform float time;
uniform sampler2D tex;

void main()
{
    float intensity = dot(norms, normalize(pointLight - pos));
    fragColor = texture(tex, UVs) * vec4((1 - 1*sin(time * 3)),0,(1 + 1*sin(time * 3)),1.0);
}
'''

fragment_shader_toonpop = '''
#version 450 core

out vec4 fragColor;

in vec2 UVs;
in vec3 norms;
in vec3 pos;

uniform vec3 pointLight;

uniform sampler2D tex;

void main()
{
    float intensity = dot(norms, normalize(pointLight - pos));
    if (intensity < 0.14) {
        fragColor = vec4(1,0,0, 1.0) / intensity;
    } else if (intensity < 0.28){
        fragColor = texture(tex, UVs) * vec4(1,0.5,0, 1.0) / intensity;
    } else if (intensity < 0.42){
        fragColor = texture(tex, UVs) * vec4(1,1,0, 1.0) / intensity;
    } else if (intensity < 0.56){
        fragColor = texture(tex, UVs) * vec4(0,1,0, 1.0) / intensity;
    } else if (intensity < 0.7){
        fragColor = texture(tex, UVs) * vec4(0,1,1, 1.0) / intensity;
    } else if (intensity < 0.84){
        fragColor = texture(tex, UVs) * vec4(0,0,1, 1.0) / intensity;
    } else {
        fragColor = texture(tex, UVs) * vec4(0.5,0,1, 1.0) / intensity;
    }
}
'''

fragment_shader_tooncrazy = '''
#version 450 core

out vec4 fragColor;

in vec2 UVs;
in vec3 norms;
in vec3 pos;

uniform vec3 pointLight;
uniform float time;
uniform sampler2D tex;

void main()
{
    float intensity = dot(norms, normalize(pointLight - pos));
    if (intensity < 0.14) {
        fragColor = texture(tex, UVs) * vec4((1 + 1*sin(time * 5)),(1 - 1*sin(time * 10)),(1 + 1*sin(time * 15)),1.0);
    } else if (intensity < 0.28){
        fragColor = texture(tex, UVs) * vec4((1 - 1*sin(time * 6)),(1 + 1*sin(time * 11)),(1 - 1*sin(time * 16)),1.0);
    } else if (intensity < 0.42){
        fragColor = texture(tex, UVs) * vec4((1 + 1*sin(time * 7)),(1 - 1*sin(time * 12)),(1 + 1*sin(time * 17)),1.0);
    } else if (intensity < 0.56){
        fragColor = texture(tex, UVs) * vec4((1 - 1*sin(time * 8)),(1 + 1*sin(time * 13)),(1 - 1*sin(time * 18)),1.0);
    } else if (intensity < 0.7){
        fragColor = texture(tex, UVs) * vec4((1 + 1*sin(time * 9)),(1 - 1*sin(time * 14)),(1 + 1*sin(time * 19)),1.0);
    } else if (intensity < 0.84){
        fragColor = texture(tex, UVs) * vec4((1 - 1*sin(time * 10)),(1 + 1*sin(time * 15)),(1 - 1*sin(time * 20)),1.0);
    } else {
        fragColor = texture(tex, UVs) * vec4((1 + 1*sin(time * 11)),(1 - 1*sin(time * 16)),(1 + 1*sin(time * 21)),1.0);
    }
}
'''

fragment_shader_tooncrazy2 = '''
#version 450 core

out vec4 fragColor;

in vec2 UVs;
in vec3 norms;
in vec3 pos;

uniform vec3 pointLight;
uniform float time;
uniform sampler2D tex;

void main()
{
    float intensity = dot(norms, normalize(pointLight - pos));
    if (intensity < 0.14) {
        fragColor = vec4((1 + 1*sin(time * 5)),(1 - 1*sin(time * 10)),(1 + 1*sin(time * 15)),1.0);
    } else if (intensity < 0.28){
        fragColor = vec4((1 - 1*sin(time * 6)),(1 + 1*sin(time * 11)),(1 - 1*sin(time * 16)),1.0);
    } else if (intensity < 0.42){
        fragColor = vec4((1 + 1*sin(time * 7)),(1 - 1*sin(time * 12)),(1 + 1*sin(time * 17)),1.0);
    } else if (intensity < 0.56){
        fragColor = vec4((1 - 1*sin(time * 8)),(1 + 1*sin(time * 13)),(1 - 1*sin(time * 18)),1.0);
    } else if (intensity < 0.7){
        fragColor = vec4((1 + 1*sin(time * 9)),(1 - 1*sin(time * 14)),(1 + 1*sin(time * 19)),1.0);
    } else if (intensity < 0.84){
        fragColor = vec4((1 - 1*sin(time * 10)),(1 + 1*sin(time * 15)),(1 - 1*sin(time * 20)),1.0);
    } else {
        fragColor = vec4((1 + 1*sin(time * 11)),(1 - 1*sin(time * 16)),(1 + 1*sin(time * 21)),1.0);
    }
}
'''
