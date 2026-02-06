import { ArrowLeft, ArrowRight } from 'lucide-react';
import { useState } from 'react';

interface Noticias {
    imagen: string;
    titulo: string;
    fuente: string;
    resumen: string;
    url: string;
    fecha_publicacion: string | Date;
    categoria: string;
}

interface Props {
    noticias: Noticias[];
}

export default function MainCarrusel({ noticias }: Props) {
    const [index, setIndex] = useState(0);
    const [isActive, setIsActive] = useState(false);

    const formatFecha = (fecha: string | Date) => {
        return new Date(fecha).toLocaleDateString('es-ES', {
            month: 'short',
            day: 'numeric',
            year: 'numeric',
        });
    };

    const coloresCategorias: Record<string, string> = {
        Tecnología: 'bg-blue-100 text-blue-700',
        Política: 'bg-red-100 text-red-700',
        Deportes: 'bg-green-100 text-green-700',
        Cultura: 'bg-purple-100 text-purple-700',
        Economia: 'bg-yellow-100 text-yellow-700',
        España: 'bg-amber-100 text-amber-700',
        Latinoamérica: 'bg-violet-100 text-violet-700',
        'Es la Mañana de Federico': 'bg-sky-100 text-sky-700',
        default: 'bg-gray-100 text-gray-700',
    };

    const remaining = noticias.length - index;
    const showMoreCard = remaining <= 3;
    const visible = showMoreCard
        ? noticias.slice(index, index + remaining - 1)
        : noticias.slice(index, index + 3);

    return (
        <section className="max-w-7xl mx-auto ">
            <div className="flex items-center justify-between pb-8">
                <div className=" p-2">
                    <h1 className="text-4xl font-bold">Más Noticias</h1>
                </div>
                <div>
                    <button
                        onClick={() => setIndex((i) => Math.max(0, i - 3))}
                        className="bg-blue-200 p-2 rounded-full cursor-pointer disabled:opacity-50 disabled:cursor-not-allowed"
                        disabled={index === 0}
                    >
                        <ArrowLeft
                            size={24}
                            className="hover:scale-110 transition-all duration-200"
                        />
                    </button>
                    <button
                        disabled={remaining <= 3}
                        onClick={() =>
                            setIndex((i) =>
                                Math.min(noticias.length - 3, index + 3)
                            )
                        }
                        className=" bg-blue-200 p-2 rounded-full ml-8 cursor-pointer disabled:opacity-50 disabled:cursor-not-allowed"
                    >
                        <ArrowRight
                            size={24}
                            className="hover:scale-110 transition-all duration-200"
                        />
                    </button>
                </div>
            </div>
            <div className=" grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 w-full ">
                {visible.map((n, i) => {
                    const catNombre = n.categoria?.trim() || 'default';
                    const estiloBadge =
                        coloresCategorias[catNombre] ||
                        coloresCategorias['default'];
                    return (
                        <div className="flex flex-col group border border-gray-200 rounded-2xl bg-white  overflow-hidden shadow-sm transition-shadow hover:shadow-md h-145.5">
                            <a
                                key={i}
                                href={n.url}
                                target="_blank"
                                className="flex flex-col h-full"
                            >
                                <div className="overflow-hidden h-64 w-full">
                                    <img
                                        src={n.imagen}
                                        alt={n.titulo}
                                        className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105"
                                        referrerPolicy="no-referrer"
                                    />
                                </div>

                                {/* Cuerpo */}
                                <div className="p-5 flex flex-col grow">
                                    <div className="flex justify-between items-center mb-4">
                                        <span
                                            className={`text-[10px] uppercase font-bold px-2 py-1 rounded-md ${estiloBadge}`}
                                        >
                                            {n.categoria}
                                        </span>
                                        <span className="text-xs text-gray-400">
                                            {formatFecha(n.fecha_publicacion)}
                                        </span>
                                    </div>
                                    <h3 className="text-xl font-bold mb-2 leading-tight group-hover:text-blue-600 transition-colors">
                                        {n.titulo}
                                    </h3>
                                    <p className="text-sm text-gray-600 line-clamp-3 mb-6 grow h-full">
                                        {n.resumen}
                                    </p>
                                    <div className="grow mt-auto" />
                                    <div className="pt-4 border-t border-gray-100 ">
                                        <span className="inline-block w-full text-center font-semibold text-sm text-blue-600 bg-blue-50 hover:bg-blue-100 rounded-lg py-2 transition-colors">
                                            {n.fuente}
                                        </span>
                                    </div>
                                </div>
                            </a>
                        </div>
                    );
                })}

                {showMoreCard && (
                    <a
                        href="/noticas"
                        className="flex items-center justify-center  border-2 border-dashed rounded-xl font-bold"
                    >
                        Más Noticias
                    </a>
                )}
            </div>
        </section>
    );
}
